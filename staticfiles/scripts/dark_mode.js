let element_html=document.getElementById("id_html");
let element_dark_mode=document.getElementById("id_dark_mode");
let element_light_mode=document.getElementById("id_light_mode");

window.addEventListener("load",function(){
	if (localStorage.getItem("mode")==="dark"){
		element_html.setAttribute("data-bs-theme","dark");
		element_light_mode.style.display="inline";
		element_dark_mode.style.display="none";
	}else{
		element_html.setAttribute("data-bs-theme","light");
		element_dark_mode.style.display="inline";
		element_light_mode.style.display="none";
	}
});

function change_theme(mode_element){
	if (mode_element.getAttribute("id")==="id_dark_mode"){
		element_html.setAttribute("data-bs-theme","dark");
		localStorage.setItem("mode","dark");
		mode_element.style.display="none";
		element_light_mode.style.display="inline";

	}else{
		element_html.setAttribute("data-bs-theme","light");
		localStorage.setItem("mode","light");
		mode_element.style.display="none";
		element_dark_mode.style.display="inline";

	}
}

element_dark_mode.addEventListener("click",function(){
	change_theme(element_dark_mode);
});
element_light_mode.addEventListener("click",function(){
	change_theme(element_light_mode);
});