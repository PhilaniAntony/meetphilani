var bannerStatus = 1;
var bannerTimeout = 2000;

window.onload =()=>{
    bannerLoop();
}

var start = setInterval(function(){
    bannerLoop();
}, bannerTimeout);

//clear internal on mouse enter and stop flow
document.getElementById('main-banner').onmouseenter = ()=> {
    clearInterval(start);
};

//mouseleave and start flow
document.getElementById("main-banner").onmouseleave = () =>{
	start = setInterval(function(){
		bannerLoop();
	}, bannerTimer);
};

//prev button to change slides
document.getElementById('button-prev').onclick =()=>{
    if(bannerStatus == 1){
        bannerStatus = 2;
    } else if(bannerStatus == 2){
        bannerStatus = 3;
    } else if (bannerStatus ==3){
        bannerStatus = 1;
    };
    bannerLoop();
};
//next button to chane slides
document.getElementById('button-next').onclick =()=>{
    bannerLoop();
};

const bannerLoop=()=>{
	if (bannerstatus == 1) {
		document.getElementById("imgban2").style.opacity = "0";
		setTimeout(function() {
			document.getElementById("imgban1").style.right = "0px";
			document.getElementById("imgban1").style.zIndex = "1000";
			document.getElementById("imgban2").style.right = "-600px";
			document.getElementById("imgban2").style.zIndex = "1500";
			document.getElementById("imgban3").style.right = "-600px";
			document.getElementById("imgban3").style.zIndex = "500";
		}, 500);
		
		setTimeout(function() {
			document.getElementById("imgban2").style.opacity = "1";	
		}, 1000);
		bannerstatus = 2;
	} //second loop
	else if (bannerstatus === 2) {
		document.getElementById("imgban3").style.opacity = "0";
		setTimeout(function() {
			document.getElementById("imgban2").style.right = "0px";
			document.getElementById("imgban2").style.zIndex = "1000";
			document.getElementById("imgban3").style.right = "-600px";
			document.getElementById("imgban3").style.zIndex = "1500";
			document.getElementById("imgban1").style.right = "-600px";
			document.getElementById("imgban1").style.zIndex = "500";
		}, 500);
		
		setTimeout(function() {
			document.getElementById("imgban3").style.opacity = "1";	
		}, 1000);
		bannerstatus = 3;
	}
	else if (bannerstatus === 3) {
		document.getElementById("imgban1").style.opacity = "0";
		setTimeout(function() {
			document.getElementById("imgban3").style.right = "0px";
			document.getElementById("imgban3").style.zIndex = "1000";
			document.getElementById("imgban1").style.right = "-600px";
			document.getElementById("imgban1").style.zIndex = "1500";
			document.getElementById("imgban2").style.right = "-600px";
			document.getElementById("imgban2").style.zIndex = "500";
		}, 500);
		
		setTimeout(function() {
			document.getElementById("imgban1").style.opacity = "1";	
		}, 1000);
		bannerstatus = 1;
	}
}




