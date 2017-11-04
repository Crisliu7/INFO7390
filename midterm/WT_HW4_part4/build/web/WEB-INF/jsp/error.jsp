<%@page import="java.sql.ResultSet"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%
    response.setHeader("Cache-Control", "no-cache");
    response.setHeader("Cache-Control", "no-store");
    response.setHeader("Pragma", "no-cache");
    response.setDateHeader("Expires", 0);
%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Error</title>
    </head>
    <body>
        <h1>Top 10 Closest Home According To Your Location</h1>
        <form name="mainPage" method="post" action="index.htm">
        
        ${sessionScope.e}
        
            <table>
                <thead>
                    <tr>
                        <td>Parcel ID</td>
                        <td>Longitude</td>
                        <td>Latitude</td>
                        <td>Distance</td>

                    </tr>
                </thead>
                <tbody>

                <<c:forEach items="${sessionScope.top10}" var="top10">
                        <tr>
                            <td>${top10.parcel_id}</td>
                            <td>${top10.longitude}</td>
                            <td>${top10.latitude}</td>
                            <td>${top10.distance}</td>
                            
                        </tr>
                    </c:forEach>

                </tbody>
            </table>
            <input type="submit" name="submit" value="Go Back To Main Page Again">
        </form>
    </body>
</html>
