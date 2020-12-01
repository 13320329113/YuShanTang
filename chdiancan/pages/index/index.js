//index.js
//获取应用实例
const app = getApp()


Page({
  data: {
   foodlist:[],
   cookerlist:[],
   pptlist:[]
  },
  
  fngetdatalist:function(){
    var that=this;
      //在此处编写请求首页菜品数据的逻辑代码
    wx.request({
      url: 'http://localhost:8000/dcapi/getdatalistbyrandom',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc);
        that.setData({
          foodlist:cc.data[0].foodlist,//把后端查询出来的菜品列表信息存放到foodlist数组中
          cookerlist:cc.data[0].cookerlist,//把后端查询出来的菜品列表信息存放到数组中
          pptlist:cc.data[0].pptlist//把后端查询出来的菜品列表信息存放到数组中
        });
      }
    });
  },

  fnsearch:function(e){
    getApp().globalData.key=e.detail.value;
    wx.switchTab({
      url: '/pages/foodlist/foodlist',
    });
  },

  fngotocooker:function(ex){
    var id=ex.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/cooker/cooker',
    })
  },
  fngotocompany:function(){
    wx.navigateTo({
      url: '/pages/company/company',
    })
  },
  fngotoroom:function(){
    wx.navigateTo({
      url: '/pages/privateroom/privateroom',
    })
  },

  fngotofoodview:function(ex){
    //通过点击事件里面的事件对象e获取组件上面绑定的属性值，这些属性属于自定义属性，必须以data-开头。
    var id=ex.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/foodview/foodview?id='+id,
    })

  },
  //事件处理函数
  bindViewTap: function() {
    wx.navigateTo({
      url: '../logs/logs'
    })
  },

  fngotocookerview:function(ex){
    //通过点击事件里面的事件对象e获取组件上面绑定的属性值，这些属性属于自定义属性，必须以data-开头。
    var id=ex.currentTarget.dataset.id;
    wx.navigateTo({
      url:'/pages/cookerview/cookerview?id='+id,
    })
  },
  
  getUserInfo: function(e) {
    
  },

  
  onLoad: function () {//页面加载的时候执行
    console.log(app.globalData.username)
    console.log(app.globalData.sex)
  },

  // fngetcookerlist:function(){
  //   var that=this;
  //     //在此处编写请求首页厨师数据的逻辑代码
  //   wx.request({
  //     url: 'http://localhost:8000/dcapi/getcookerlistbyrandom',
  //     method: 'POST',
  //     data: {
        
  //     },
  //     header: {
  //       'content-type': 'application/x-www-form-urlencoded' // 默认值
  //     },
  //     dataType: 'json',
  //     success(cc) {
  //       console.log(cc.data);
  //       that.setData({
  //         cookerlist:cc.data//把后端查询出来的菜品列表信息存放到cookerlist数组中
  //       });
  //     }
  //   });
  // },

  

  fngetfoodlist:function(){
    var that=this;
    wx.request({
      url: 'http://localhost:8000/dcapi/getfoodlistbyrandom',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
          foodlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
        });
        that.fngetcookerlist();
      }
    });
  },
  onShow:function(){
    this.fngetdatalist();
    
  },

  fngetpptlistbyrandom:function(){
    var that=this; 
    wx.request({
      url: 'http://localhost:8000/dcapi/getpptlistbyrandom',
      method: 'POST',
      data: {
        
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
          pptlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
        });
      }
    });
  },


  
  fngetdata:function()
  {
    var that=this;
    var key=getApp().globalData.key;
    if(key==undefined||key==null||key=="undefined")
    {
      key="";
    }
    wx.request({
      url: 'http://localhost:8000/dcapi/getcookerlist',
      method: 'POST',
      data: {
        key:key
      },
      header: {
        'content-type': 'application/x-www-form-urlencoded' // 默认值
      },
      dataType: 'json',
      success(cc) {
        console.log(cc.data);
        that.setData({
          cookerlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
        });
      }
    });
  },









  // fngetpptlistbyrandom:function(){
  //   var that=this; 
  //   wx.request({
  //     url: 'http://localhost:8000/dcapi/getpptlistbyrandom',
  //     method: 'POST',
  //     data: {
        
  //     },
  //     header: {
  //       'content-type': 'application/x-www-form-urlencoded' // 默认值
  //     },
  //     dataType: 'json',
  //     success(cc) {
  //       console.log(cc.data);
  //       that.setData({
  //         pptlist:cc.data//把后端查询出来的菜品列表信息存放到foodlist数组中
  //       });
  //     }
  //   });
  // },



  fngototabs:function(ex){
    //通过点击事件里面的事件对象e获取组件上面绑定的属性值，这些属性属于自定义属性，必须以data-开头。
    var id=ex.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/tabs/tabs?id='+id,
    })

  },

  fngotovtabs:function(ex){
    //通过点击事件里面的事件对象e获取组件上面绑定的属性值，这些属性属于自定义属性，必须以data-开头。
    var id=ex.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/vtabs/vtabs?id='+id,
    })

  },

  fngotostlist:function(ex){
    //通过点击事件里面的事件对象e获取组件上面绑定的属性值，这些属性属于自定义属性，必须以data-开头。
    var id=ex.currentTarget.dataset.id;
    wx.navigateTo({
      url: '/pages/Starlist/Starlist?id='+id,
    })

  },
})