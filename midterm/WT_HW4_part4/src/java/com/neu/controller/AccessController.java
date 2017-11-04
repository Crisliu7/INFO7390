/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.neu.controller;

import com.neu.bean.Home;
import com.neu.bean.Order;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;

/**
 *
 * @author Sc Zhang
 */
public class AccessController extends AbstractController {

    public AccessController() {
    }

    protected ModelAndView handleRequestInternal(
            HttpServletRequest request,
            HttpServletResponse response) throws Exception {

        HttpSession session = request.getSession(true);

        String latitude = request.getParameter("latitude");
        String longitude = request.getParameter("longitude");
        double given_lat = Double.parseDouble(latitude);
        double given_lon = Double.parseDouble(longitude);
        ModelAndView mv = new ModelAndView();
        Class.forName("org.relique.jdbc.csv.CsvDriver");

        Connection connCSV = DriverManager.getConnection("jdbc:relique:csv:/Users/QiYuBin/neu.edu/WT");
        Connection connDB = DriverManager.getConnection("jdbc:mysql://localhost:3306/2017_properties?rewriteBatchedStatements=true", "root", "sicheng");

        connDB.setAutoCommit(false);

        String sql = "SELECT parcel_id, latitude, longitude FROM location "
                + "WHERE latitude >= ("
                + given_lat + " - 5) AND latitude <= ( "
                + given_lat + " +5)"
                + " AND longitude >= (" + given_lon
                + "- 10) AND longitude <= (" + given_lon
                + "+ 10);";
        PreparedStatement stmt = connDB.prepareStatement(sql);
        ResultSet rs1 = stmt.executeQuery();
        ArrayList<Home> homeList = new ArrayList<>();
//        String insql = "insert into Orders (SalesOrderID, RevisionNumber, OrderDate, DueDate, ShipDate, Status, OnlineOrderFlag, SalesOrderNumber, PurchaseOrderNumber, AccountNumber, CustomerID, SalesPersonID, TerritoryID, BillToAddressID, ShipToAddressID, ShipMethodID, CreditCardID, CreditCardApprovalCode, CurrencyRateID, SubTotal, TaxAmt, Freight, TotalDue, Comment, ModifiedDate) " + "values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
//        PreparedStatement ps = connDB.prepareStatement(insql);
        //rs1.

        while (rs1.next()) {
            Home h = new Home();
////            String pt1 = "SET @pt1 = ST_GeomFromText('POINT(" + given_lon+" " + given_lat + ")');";
////            String pt2 = "SET @pt2 = ST_GeomFromText('POINT("+ Double.parseDouble(rs1.getString(2))+" " + Double.parseDouble(rs1.getString(3)) + ")');";
//            String calculation = "SELECT ST_Distance_Sphere(ST_GeomFromText('POINT(" + given_lon+" " + given_lat + ")'), ST_GeomFromText('POINT("+ Double.parseDouble(rs1.getString(2))+" " + Double.parseDouble(rs1.getString(3)) + ")'));";
//
//            System.out.println(calculation);
//            PreparedStatement s3 = connDB.prepareStatement(calculation);
//           
//            ResultSet rs2 = s3.executeQuery();
            h.setParcel_id(rs1.getString(1));

            double R = 6371e3;

            double cal_lon = Double.parseDouble(rs1.getString(2));
            double cal_lat = Double.parseDouble(rs1.getString(3));

            double theta = given_lon - cal_lon;

            double distance = (Math.sin(Math.toRadians(given_lat)) * Math.sin(Math.toRadians(cal_lat))) + (Math.cos(Math.toRadians(given_lat)) * Math.cos(Math.toRadians(cal_lat)) * Math.cos(Math.toRadians(theta)));
            distance = Math.acos(distance);
            distance = Math.toDegrees(distance);
            distance = distance * 60 * 1.1515;
            h.setDistance(distance);
            h.setLatitude(rs1.getString(2));
            h.setLongitude(rs1.getString(3));
            homeList.add(h);
//            Order o = new Order();
//            o.setSalesOrderId(rs.getString(1));
//            o.setRevisionNumber(rs.getString(2));
//            o.setOrderDate(rs.getString(3));
//            o.setDueDate(rs.getString(4));
//            o.setShipDate(rs.getString(5));
//            o.setStatus(rs.getString(6));
//            o.setOnlineOrder(rs.getString(7));
//            o.setSalesOrderNumber(rs.getString(8));
//            o.setPurchaseOrderNumber(rs.getString(9));
//            o.setAccountNumber(rs.getString(10));
//            o.setCustomerID(rs.getString(11));
//            o.setSalesPersonID(rs.getString(12));
//            o.setTerritoryID(rs.getString(13));
//            o.setBillToAddressID(rs.getString(14));
//            o.setShipToAddressID(rs.getString(15));
//            o.setShipMethodID(rs.getString(16));
//            o.setCreditCardID(rs.getString(17));
//            o.setCreditCardApprovalCode(rs.getString(18));
//            o.setCurrencyRateID(rs.getString(19));
//            o.setSubTotal(Float.parseFloat(rs.getString(20)));
//            o.setTaxAmt(Float.parseFloat(rs.getString(21)));
//            o.setFreight(Float.parseFloat(rs.getString(22)));
//            o.setTotalDue(Float.parseFloat(rs.getString(23)));
//            o.setComment(rs.getString(24));
//            o.setModifiedDate(rs.getString(25));
//            orderList.add(o);

//            String salesOrderID = rs.getString(1);
//            String revisionNumber = rs.getString(2);
//            String orderDate = rs.getString(3);
//            String dueDate = rs.getString(4);
//            String shipDate = rs.getString(5);
//            String status = rs.getString(6);
//            String onlineOrderFlag = rs.getString(7);
//            String salesOrderNumber = rs.getString(8);
//            String purchaseOrderNumber = rs.getString(9);
//            String accountNumber = rs.getString(10);
//            String customerID = rs.getString(11);
//            String salesPersonID = rs.getString(12);
//            String territoryID = rs.getString(13);
//            String billToAddressID = rs.getString(14);
//            String shipToAddressID = rs.getString(15);
//            String shipMethodID = rs.getString(16);
//            String creditCardID = rs.getString(17);
//            String creditCardApprovalCode = rs.getString(18);
//            String currencyRateID = rs.getString(19);
//            String subTotal = rs.getString(20);
//            String taxAmt = rs.getString(21);
//            String freight = rs.getString(22);
//            String totalDue = rs.getString(23);
//            String comment = rs.getString(24);
//            String modifiedDate = rs.getString(25);
//            
//            
//            
//            ps.setString(1, salesOrderID);
//            ps.setString(2, revisionNumber);
//            ps.setString(3, orderDate);
//            ps.setString(4, dueDate);
//            ps.setString(5, shipDate);
//            ps.setString(6, status);
//            ps.setString(7, onlineOrderFlag);
//            ps.setString(8, salesOrderNumber);
//            ps.setString(9, purchaseOrderNumber);
//            ps.setString(10, accountNumber);
//            ps.setString(11, customerID);
//            ps.setString(12, salesPersonID);
//            ps.setString(13, territoryID);
//            ps.setString(14, billToAddressID);
//            ps.setString(15, shipToAddressID);
//            ps.setString(16, shipMethodID);
//            ps.setString(17, creditCardID);
//            ps.setString(18, creditCardApprovalCode);
//            ps.setString(19, currencyRateID);
//            ps.setString(20, subTotal);
//            ps.setString(21, taxAmt);
//            ps.setString(22, freight);
//            ps.setString(23, totalDue);
//            ps.setString(24, comment);
//            ps.setString(25, modifiedDate);
//          ps.executeUpdate();
//            
//            
//        
//        ps.addBatch();
//        
//        ps.executeBatch();
            connDB.commit();
        }

        Collections.sort(homeList, new Comparator<Home>() {
            @Override
            public int compare(Home h1, Home h2) {
                return Double.compare(h1.getDistance(), h2.getDistance());
            }
        });
        ArrayList<Home> top10 = new ArrayList<>();
        String e = "";
        if (homeList.size() > 0) {
            for (int i = 0; i < 10 && i <= homeList.size(); i++) {
                top10.add(homeList.get(i));
            }
        }else{
            e = "NO HOME FOUNDED NEARBY";
        }
        session.setAttribute("top10", top10);
        session.setAttribute("rs1", rs1);
        session.setAttribute("homeList", homeList.size());

        session.setAttribute("given_lat", given_lat);
        session.setAttribute("e", e);
//        session.setAttribute("ps", ps);

        connCSV.close();
        connDB.close();

        mv.setViewName("error");

        return mv;

    }

}
