var express=require('express'),
    app=express(),
    methodOverride=require('method-override'),
    errorhandler=require('errorhandler');

app.use(methodOverride());
app.use(express.static(__dirname+'/../public'));
app.set('env','production');
app.set('views',__dirname+'/../public');
app.set('view engine','html');
process.on('uncaughtException',function(err){
    console.log('error occurs');
});
var data=require('./db.js'),
    User=data.User,
    Book=data.Book;
User.findOne({name:'suemi'},function(err,doc){
    if(!err&!doc){
        var user= new User({name:'suemi',passwd:'******'});
        user.save();
    }
});
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
    User.findOne({name:'suemi'},function(err,doc){
        if(err) res.send('fail');
        else res.send(doc);
    });
});
app.post('/write',function(req,res){
    var tmp=Math.floor(Math.random()*10000);
    Book.findOne({serial:tmp},function(err,doc){
        if(!doc){
           (new  Book({serial:tmp,money:400})).save(function(err,doc){
                if(!err) res.send('success');
                else res.send('fail');
            });
        }
        else{
            doc.money=400;
            doc.save(function(err,doc){
                if(!err) res.send('success');
                else res.send('fail');
            });
        }
    });
});
app.get('/chain',function(req,res,next){
    req.str="";
    next();
});
app.get('/chain',function(req,res,next){
    req.str+="0";
    next();
});
app.get('/chain',function(req,res,next){
    req.str+="1";
    next();
});
app.get('/chain',function(req,res,next){
    req.str+="2";
    next();
});
app.get('/chain',function(req,res){
    res.send(req.str);
});
module.exports=app;
app.listen(3000,function(){
    console.log('Server starts listen to 3000');
});
