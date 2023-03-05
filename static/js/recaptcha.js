function onClick(e) {
    e.preventDefault();
    grecaptcha.ready(function() {
      grecaptcha.execute('6LcbSdEkAAAAADYWlO-19otCnqIA_jilUxilvkl8', {action: 'submit'}).then(function(token) {
          // Add your logic to submit to your backend server here.
      });
    });
  }