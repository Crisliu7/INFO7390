/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.neu.filter;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletRequestWrapper;

/**
 *
 * @author Sc Zhang
 */
public class XssHttpServlet extends HttpServletRequestWrapper {

    HttpServletRequest orgRequest = null;

    public XssHttpServlet(HttpServletRequest request) {
        super(request);
        orgRequest = request;
    }

//make parameters and parameter names filter,
//if need orginal values, by super.getParameterValues(name);  
    
    public String getParameter(String name) {
        String value = super.getParameter(xss(name));
        if (value != null) {
            value = xss(value);
        }
        return value;
    }

    public String[] getParameterValues(String name){
        String[] values = super.getParameterValues(xss(name));
        for(int i=0;i<values.length;i++)
        {
            if (values != null) {
                values[i]=xss(values[i]);
            }
        }
        return values;
    }
    public String getHeader(String name) {
        String value = super.getHeader(xss(name));
        if (value != null) {
            value = xss(value);
        }
        return value;
    }

    //change the letters which can make xss
    public static String xss(String s) {
        if (s == null || s.isEmpty()) {
            return s;
        }
        StringBuilder sb = new StringBuilder(s.length() + 16);
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            switch (c) {
                case '<':
                    sb.append('_');

                    break;
                case '>':
                    sb.append('_');
                    break;
                case '\'':
                    sb.append('_');
                    break;
                case '\"':
                    sb.append('_');
                    break;
                case '&':
                    sb.append('_');
                    break;
                case '\\':
                    sb.append('_');
                    break;
                case '#':
                    sb.append('_');
                    break;
                case '=':
                    sb.append('=');
                    break;
                default:
                    sb.append(c);
                    break;
            }

        }

        return sb.toString();
    }

    public HttpServletRequest getOrgRequest() {

        return orgRequest;
    }

    public static HttpServletRequest getOrgRequest(HttpServletRequest req) {
        if (req instanceof XssHttpServlet) {
            return ((XssHttpServlet) req).getOrgRequest();
        }
        return req;
    }
}



