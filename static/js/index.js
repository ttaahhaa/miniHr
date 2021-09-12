let uploadedInfo = document.getElementById("uploaded")
let firstName = document.getElementById("firstName")
let lastName = document.getElementById("lastName")
let email = document.getElementById("email")
let yearsOfExperience = document.getElementById("yearsOfExperience")
let department = document.getElementById("Department")
let bdate = document.getElementById("bdate")
let resStatus = document.getElementById("resStatus")

let submit = document.getElementById("submit")

document.getElementById('submit').onclick = function () {
 const formData = new FormData()
  formData.append('cv', document.getElementById('cvFile').files[0])
    console.log(firstName)
        console.log(firstName.value)

    formData.append("firstName", firstName.value)
    formData.append("lastName", lastName.value)
    formData.append("email", email.value)
    formData.append("yearsOfExperience", yearsOfExperience.value)
    formData.append("department", department.value)
    formData.append("bdate", bdate.value)

  fetch('http://127.0.0.1:5000/postApplication', {
    method: 'POST',
    body: formData
  })
  .then((response) => {
      if(response.status ==201){
          resStatus.innerHTML = "The Application submitted successfully "
          resStatus.style.setProperty("color", "green", "important");
      }
      else{
     resStatus.innerHTML = "Something went wrong !!!"
          resStatus.style.setProperty("color", "red", "important");
      }
  })
}
