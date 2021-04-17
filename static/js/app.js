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
      subgenre = response.data.body[0]
      rating = response.data.body[1]
      $('#subgenre').fadeOut(500, function() {
        $(this).html("<h2> Your book belongs in the science fiction subgenre: " + subgenre + "</h2>").fadeIn(500);
      });
      $('#rating').fadeOut(500, function() {
        $(this).html("<h2> We predict the success of your book to be: " + rating + "</h2>").fadeIn(500);
      });
      console.log(subgenre)
    });
});
