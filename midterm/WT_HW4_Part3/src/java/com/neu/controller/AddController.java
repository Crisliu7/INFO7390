/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.neu.controller;

import com.neu.bean.Book;
import java.sql.SQLException;
import java.text.SimpleDateFormat;
import java.util.Date;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.sql.DataSource;
import org.apache.commons.dbutils.QueryRunner;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;

/**
 *
 * @author Sc Zhang
 */
public class AddController extends AbstractController {

    public AddController() {
    }

    protected ModelAndView handleRequestInternal(
            HttpServletRequest request,
            HttpServletResponse response) throws Exception {
        DataSource ds = (DataSource) this.getApplicationContext().getBean("myDataSource");

        HttpSession session = request.getSession(true);

        ModelAndView mv = new ModelAndView();
        QueryRunner run = new QueryRunner(ds);
        
        try{
        String q = String.valueOf(session.getAttribute("quantity"));
        int quantity = Integer.valueOf(q);

        String[] isbn = request.getParameterValues("isbn");
        String[] title = request.getParameterValues("title");
        String[] author = request.getParameterValues("authors");
        String[] tempPrice = request.getParameterValues("price");
        float[] price = new float[quantity];
        if (isbn == null || title == null || author == null || tempPrice == null || price == null) {
            mv.setViewName("error");
        } else {

            for (int i = 0; i < quantity; i++) {
                Book book = new Book();
                book.setIsbn(isbn[i]);
                book.setTitle(title[i]);
                book.setAuthor(author[i]);
                price[i] = Float.valueOf(tempPrice[i]);
                book.setPrice(price[i]);

                Object[] params = new Object[4];
                params[0] = isbn[i];
                params[1] = title[i];
                Date d = new Date();
                params[2] = author[i];
                params[3] = tempPrice[i];
                run.update("Insert into book (isbn,title,authors,price) values(?,?,?,?)", params);
            }
            mv.setViewName("success");
        }
        } catch (Exception e){
            mv.setViewName("error");
        }
        return mv;
    }
}
