function check_titleofblog(){
	let element=document.getElementById("id_titleofblog")
	element.classList.add("border")
	element.classList.add("border-danger")
}
function check_titleofblog_valid(){
	let element=document.getElementById("id_titleofblog")
	element.classList.remove("border")
	element.classList.remove("border-danger")
}

function check_image(){
	let element=document.getElementById("id_image")
	element.classList.add("border")
	element.classList.add("border-danger")
}