console.log("aaaaa")
let container = document.getElementById("container_inner");
window.onload = ()=>{
fetch('http://127.0.0.1:5000/data', {
  method: "GET",
  headers: {"Content-type": "application/json;charset=UTF-8","X-ADMIN":"1"}
})
.then(response => response.json())
.then(res =>{
    const parsed = JSON.parse(res)

   for (let i=0; i<parsed.length; i++){
   container.innerHTML+= showApplicants(parsed[i])
   }
   })
.catch(err => console.log(err));
}

/*document.addEventListener("click", (event) => {
            console.log("eventListener")
            // if the user clicks one of the download buttons. (the id of download buttons' numbers )
            if ((event.target.id).match('^[0-9]+$') != null) {
               console.log("hiiiiiiiiiii ", event.target.id)
            }})*/

function showApplicants(data_i) {
    console.log("==========>", data_i["first_name"])
    return `
        <div class="row_me">
            <span>${data_i['first_name']} ${data_i['last_name']}</span>
            <span>${data_i['bdate']}</span>
            <span>${data_i['yearsOfExperience']}</span>
            <span>${data_i['departmentID']}</span>
            <a href='hr/${data_i['ID']}' download><button class ='btn btn-group'>Download CV</button></a>
            <hr>
        </div>
        `
}