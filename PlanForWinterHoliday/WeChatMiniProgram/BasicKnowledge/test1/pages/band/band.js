// pages/band/band.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    message:"哈哈哈哈",
    name:"",
    path:""
  },
  changData:function(){
    console.log(this.data.message);
    this.setData({message:"呵呵呵呵"})
  },
  getUsername:function(){
    var that=this;
    wx.getUserInfo({
      success:function(res){
        console.log("success",res);
        that.setData({
          name:res.userInfo.nickName,
          path:res.userInfo.avatarUrl
        });
      },
      fail:function(res){
        console.log("fail",res)
      }
    })

  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})