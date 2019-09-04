// var buttons = document.querySelectorAll(".radmenu a");
//
// for (var i=0, l=buttons.length; i<l; i++) {
//   var button = buttons[i];
//   button.onclick = setSelected;
// }
//
// $("#show").on("click",function () {
//     console.log("aaa");
// })
//
// function setSelected(e) {
//     console.log("ssss");
//     if (this.classList.contains("selected")) {
//       this.classList.remove("selected");
//       $(".show").text("手动");
//       // if (!this.parentNode.classList.contains("radmenu")) {
//       //   this.parentNode.parentNode.parentNode.querySelector("a").classList.add("selected")
//       // } else {
//       //   this.classList.add("show");
//       // }
//     } else {
//       this.classList.add("selected");
//       $(".show").text("自动");
//
//
//       // if (!this.parentNode.classList.contains("radmenu")) {
//       //   this.parentNode.parentNode.parentNode.querySelector("a").classList.remove("selected")
//       // } else {
//       //   this.classList.remove("show");
//       // }
//     }
//     return false;
// }