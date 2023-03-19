
// Console-Logging functionality remains for ease of understanding functions.

let num1=0,num2=0

document.getElementById("addition").onclick=function(){
    let num1=document.getElementById("number1").value;
    let num2=document.getElementById("number2").value;

    let n1=parseFloat(num1);
    let n2=parseFloat(num2);
    let result = n1+n2;
    document.getElementById("result").innerHTML=result;


    console.log("First Number = ",n1,"Second Number = ",n2);
    console.log(n1,"+",n2,"=",result);
}

document.getElementById("subtraction").onclick=function(){
    let num1=document.getElementById("number1").value;
    let num2=document.getElementById("number2").value;

    let n1=parseFloat(num1);
    let n2=parseFloat(num2);
    let result = n1-n2;
    document.getElementById("result").innerHTML=result;

    console.log("First Number = ",n1,"Second Number = ",n2);
    console.log(n1,"-",n2,"=",result);
}

document.getElementById("multiplication").onclick=function(){
    let num1=document.getElementById("number1").value;
    let num2=document.getElementById("number2").value;

    let n1=parseFloat(num1);
    let n2=parseFloat(num2);
    let result = n1*n2;
    document.getElementById("result").innerHTML=result;

    console.log("First Number = ",n1,"Second Number = ",n2);
    console.log(n1,"x",n2,"=",result)
}

document.getElementById("division").onclick=function(){
    let num1=document.getElementById("number1").value;
    let num2=document.getElementById("number2").value;

    let n1=parseFloat(num1);
    let n2=parseFloat(num2);
    let result = n1/n2;
    document.getElementById("result").innerHTML=result;

    console.log("First Number = ",n1,"Second Number = ",n2);
    console.log(n1,"÷",n2,"=",result)
}

document.getElementById("modulo").onclick=function(){
    let num1=document.getElementById("number1").value;
    let num2=document.getElementById("number2").value;

    let n1=parseFloat(num1);
    let n2=parseFloat(num2);
    let result = n1%n2;
    document.getElementById("result").innerHTML=result;

    console.log("First Number = ",n1,"Second Number = ",n2);
    console.log(n1,"%",n2,"has a modulo of ",result);
}

document.getElementById("clear").onclick=function(){
    document.getElementById("number1").value="";
    document.getElementById("number2").value="";
    document.getElementById("result").innerHTML="";
}

document.getElementById("close").onclick=function(){
    document.body.innerHTML=""
    thankyou=document.createElement("h1");
    thankyou.innerHTML="Thank you for using this Calculator Application!"
    document.body.appendChild(thankyou);
}