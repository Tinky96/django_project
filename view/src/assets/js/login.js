// 悬浮登录窗口
document.addEventListener('DOMContentLoaded', function() {  
    var loginButton = document.getElementById('loginButton');  
    var loginContainer = document.querySelector('.login-container');  
    var closeBtn = document.querySelector('.close-btn');  
  
    loginButton.addEventListener('click', function(e) {  
        e.preventDefault();  
        showLogin();  
    });  
   
    closeBtn.addEventListener('click', function() {  
        hideLogin();  
    });  
  
    function showLogin() {  
        loginContainer.style.display = 'block';  
        document.body.style.overflow = 'auto'; // 隐藏滚动条  
    }  
  
    function hideLogin() {  
        loginContainer.style.display = 'none';  
    }  
});  



  $(document).ready(function() {  
    $('#login-btn').click(function(e) {  
      e.preventDefault(); // 阻止按钮的默认行为  
    
      var username = $('input[name="username"]').val();  
      var password = $('input[name="password"]').val();  
    
      // 发起AJAX POST请求  
      $.ajax({  
        type: 'POST',  
        data: {  
          username: username,  
          password: password,  
          csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() // 添加CSRF令牌  
        },  
        success: function(response) {  
          if (response.success) {  
            $('#login-message').text('登录成功！');  
            sessionStorage.setItem('user_id', response.user_name); // 将用户名保存在sessionStorage中  
            location.reload();  
          } else {  
            alert('账号或密码错误');  
            location.reload();  
            $('#login-message').text('登录失败：' + response.error);  
          }  
        },  
        error: function(xhr, status, error) {  
          // 请求失败时的处理  
          $('#login-message').text('请求失败：' + error);  
        }  
      });  
    });  
    
    // 在页面加载时检查session状态  
    window.onload = function() {  
      if (sessionStorage.getItem('user_id')) {  
        // 用户已登录  
        // 执行相应操作  
        var username = sessionStorage.getItem('user_id');  
        // 根据用户名进行后续操作  
        // ...  
      } else {  
        // 用户未登录  
        // 执行相应操作  
      }  
    };  
  });  
  
  $(document).ready(function() {  
    // 在页面加载时检查session状态  
    if (sessionStorage.getItem('user_id')) {  
      // 用户已登录  
      var username = sessionStorage.getItem('user_id');  
      var initials = username.charAt(0).toUpperCase();  
      $('.user-initials').text(initials);  
    } else {  
      // 用户未登录  
      $('.user-initials').text('登录');  
    }  
  });  
  

  // 再用户界面显示用户名
  $(document).ready(function() {  
    // 在页面加载时检查session状态  
    if (sessionStorage.getItem('user_id')) {  
      // 用户已登录  
      var username = sessionStorage.getItem('user_id');  
      $('.user-name').text(username);  
    } else {  
      // 用户未登录  
      $('.user-name').text('用户名');  
    }  
  });  