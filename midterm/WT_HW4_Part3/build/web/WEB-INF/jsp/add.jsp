<%-- 
    Document   : Add
    Created on : Feb 12, 2017, 12:53:47 PM
    Author     : Sc Zhang
--%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Book Details</title>
    </head>
    <body>
        <h2><b>Please implement the details</b></h2>
        
            <form name='add' method="post" action="add.htm">
                <table>
                    <thead>
                        <tr >
                            <td>ISBN</td>
                            <td>Title</td>
                            <td>Author</td>
                            <td>price</td>
                        </tr>
                    </thead>
                    <tbody>
                    
                    <c:forEach var="i" begin="1" end= "${sessionScope.quantity}">
            <tr>
                <td><input type='text' name='isbn' required="true"></td>
                <td><input type='text' name='title' required="true"></td>
                <td><input type='text' name='authors' required="true"></td>
                <td><input type='number' name='price' required="true"></td>
            </tr>
        </c:forEach>
                    
                    </tbody>
                </table>
                <input type="submit" name="submit" value="Confirm">
            </form>
    </body>
</html>
