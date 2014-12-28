var express=require('express'),
    app=express(),
    methodOverride=require('method-override'),
    errorhandler=require('errorhandler');

app.use(methodOverride());
app.use(express.static(__dirname+'/../public'));
app.set('env','production');
app.set('views',__dirname+'/../public');
app.set('view engine','html');
if('production'==app.get('env')){
    app.use(errorhandler());
    console.log('error handler turn on');
}
app.get('/',function(req,res){
    res.render('index');
});
app.get('/str',function(req,res){
    res.send('hello,world');
});
app.get('/json',function(req,res){
    res.send({msg:'Hello,World!'});
});
app.get('/read',function(req,res){
});
app.post('/write',function(req,res){

});
module.exports=app;
app.listen(3000,function(){
    console.log('Server starts listen to 3000');
});
