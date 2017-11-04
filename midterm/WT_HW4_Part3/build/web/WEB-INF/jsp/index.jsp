<%@page import="java.util.ArrayList"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd">

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Welcome to REST API</title>
    </head>

    <body>
        <div>
            <h2><b>Please enter the housing data that you want to analyze</b></h2>
            <form name="mainPage" method="post" action="access.htm">
                <table>
                    <thead>
                        <tr >
                            <td>Tax Amount</td>
                            <td>Longitude</td>
                            <td>Latitude</td>
                            <td>Bedroom Count</td>
                            <td>Finished Square Feet</td>
                            <td>Lot Size Square Feet</td>
                            <td>Zip Code</td>
                            <td>Deal Month</td>
                            <td>Built Year</td>
                            
                        </tr>
                    </thead>
                    <tbody>
                    
                        <tr >
                        <td><input type="number" name="taxamount" required="true"></td>
                        <td><input type="number" name="longitude" required="true"></td>
                        <td><input type="number" name="latitude" required="true"></td> 
                        <td><input type="number" name="finishedsquarefeet12" required="true"></td>
                        <td><input type="number" name="lotsizesquarefeet" required="true"></td>
                        <td><input type="number" name="regionidzip" required="true"></td>
                        <td><input type="number" name="month" required="true"></td>
                        <td><input type="number" name="yearbuilt" required="true"></td>
                        </tr>
                  
                    </tbody>
                </table>
            <input type="submit" name="submit" value="Confirm">
            </form>
            

        </div>
        
        <div>
            <h2><b>Please enter the housing data that you want to analyze</b></h2>
        </div>
    </body>
</html>
