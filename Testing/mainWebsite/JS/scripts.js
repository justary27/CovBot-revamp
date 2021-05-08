window.addEventListener('scroll', function () {
    let header = document.querySelector('header');
    let windowPosition = window.scrollY >10;
    header.classList.toggle('scrolling-active', windowPosition);
})

document.getElementById("div1").onmouseenter=function(){
    document.getElementById("div7").style.display="flex"
    document.getElementById("div8").style.display="none"
    document.getElementById("div9").style.display="none"
    document.getElementById("div10").style.display="none"
    document.getElementById("div11").style.display="none"
    document.getElementById("div12").style.display="none"
}

document.getElementById("div2").onmouseenter=function(){
    document.getElementById("div8").style.display="flex"
    document.getElementById("div7").style.display="none"
    document.getElementById("div9").style.display="none"
    document.getElementById("div10").style.display="none"
    document.getElementById("div11").style.display="none"
    document.getElementById("div12").style.display="none"
}

document.getElementById("div3").onmouseenter=function(){
    document.getElementById("div9").style.display="flex"
    document.getElementById("div8").style.display="none"
    document.getElementById("div7").style.display="none"
    document.getElementById("div10").style.display="none"
    document.getElementById("div11").style.display="none"
    document.getElementById("div12").style.display="none"
}

document.getElementById("div4").onmouseenter=function(){
    document.getElementById("div10").style.display="flex"
    document.getElementById("div8").style.display="none"
    document.getElementById("div9").style.display="none"
    document.getElementById("div7").style.display="none"
    document.getElementById("div11").style.display="none"
    document.getElementById("div12").style.display="none"
}

document.getElementById("div5").onmouseenter=function(){
    document.getElementById("div11").style.display="flex"
    document.getElementById("div8").style.display="none"
    document.getElementById("div9").style.display="none"
    document.getElementById("div10").style.display="none"
    document.getElementById("div7").style.display="none"
    document.getElementById("div12").style.display="none"
}

document.getElementById("div6").onmouseenter=function(){
    document.getElementById("div12").style.display="flex"
    document.getElementById("div8").style.display="none"
    document.getElementById("div9").style.display="none"
    document.getElementById("div10").style.display="none"
    document.getElementById("div11").style.display="none"
    document.getElementById("div7").style.display="none"
}



// document.getElementById("body").onmouseover=function(){
//     document.getElementById("div7").style.display="none"
//     document.getElementById("div8").style.display="none"
//     document.getElementById("div9").style.display="none"
//     document.getElementById("div10").style.display="none"
//     document.getElementById("div11").style.display="none"
//     document.getElementById("div12").style.display="none"
// }

var scrollToTopBtn = document.getElementById("scrollToTopBtn")
var rootElement = document.documentElement

function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  })
}
scrollToTopBtn.addEventListener("click", scrollToTop)