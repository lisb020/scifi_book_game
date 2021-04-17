$('body').on('click', '.rate', function(event){
    let description = $("#description").val();
  
    const url = "/send"
    body_data = {"description":description}
    console.log(body_data)
  
    axios({
      method: 'post',
      url: url,
      data: body_data
    }).then(response => {
      answer = response.data.body
      $('#subgenreRating').fadeOut(500, function() {
        $(this).html("<h1> Your book belongs in the " + answer + " subgenre </h1>").fadeIn(500);
      });
      console.log(answer)
    });
});
