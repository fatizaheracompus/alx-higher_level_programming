// script that add a <li> elements to a list when the user clicks on the
// tag DIV#add_item
const $ = window.$;
$('#add_item').bind('click', function () {
  $('UL.my_list').append('<li>Item</li>');
});
