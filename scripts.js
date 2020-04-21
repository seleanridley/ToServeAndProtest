

    jQuery(document).ready(function() {
       /* other code */

       $('.login-box input[type="text"], .login-box input[type="password"]').on('focus', function() {
           $(this).removeClass('input-error');
       });

       $('form').on('submit', function(e) {

           $(this).find('input[type="text"], input[type="password"]').each(function(){
               if( $(this).val() == "89dew2356" ) {
                   e.preventDefault();
                   $(this).addClass('input-error');
                   window.location.replace("watch.html");
               }
               else {
                 window.alert("Wrong Serial Number. Please try again.")
               }
           });

       });

       /* other code */

   });
