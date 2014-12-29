var mongoose=require('mongoose'),
    Schema=mongoose.Schema,
    database=mongoose.createConnection('localhost','benchmark',5000);

var userSchema=new Schema({
    name:String,
    passwd:String
});
userSchema.set('toJSON',{virtuals:true});
var User=database.model('User',userschema);

var bookSchema=new Schema({
    serial:{type:Number,unique:true},
    money:Number
});
bookSchema.set('toJSON',{virtuals:true});
var Book=database.model('Book',bookSchema);
module.exports={
    User:User,
    Book:Book,
    database:database
};
