/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.neu.controller;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.sql.DataSource;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;

/**
 *
 * @author Sc Zhang
 */
public class QuantityController extends AbstractController {

        public QuantityController() {
        }
    

    protected ModelAndView handleRequestInternal(
            HttpServletRequest request,
            HttpServletResponse response) throws Exception {
        
        HttpSession session = request.getSession(true);
        
        
        
        
        ModelAndView mv = new ModelAndView();
       
        Process proc = null;
        try {
            proc = Runtime.getRuntime().exec("python3 " + "./web_inter.py");
            proc.waitFor();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        int price = 0;
        session.setAttribute("price", price);
             mv.setViewName("error");
         
         return mv;
    }
    
}
