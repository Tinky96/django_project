@startuml  
  
!define Table(name, desc) class name as "desc" << (T,orange) >>  
!define PK(x) <u>x</u>  
!define FK(x) <color:green>x</color>  
  
Table(User, "User") {  
  PK(user_id) int  
  username string  
  password string  
  email string  
  contact string  
}  
  
Table(GameAccount, "Game Account") {  
  PK(account_id) int  
  game_name string  
  account_level int  
  items string  
  FK(seller_id) int  
}  
  
Table(TransactionHistory, "Transaction History") {  
  PK(transaction_id) int  
  FK(buyer_id) int  
  FK(seller_id) int  
  transaction_time datetime  
  transaction_amount float  
}  
  
Table(PaymentHistory, "Payment History") {  
  PK(payment_id) int  
  FK(user_id) int  
  payment_method string  
  payment_amount float  
  payment_time datetime  
}  
  
Table(Review, "Review") {  
  PK(review_id) int  
  FK(transaction_id) int  
  review_content string  
  review_rating int  
}  
  
Table(Message, "Message") {  
  PK(message_id) int  
  FK(sender_id) int  
  FK(receiver_id) int  
  message_content string  
  message_time datetime  
}  
  
User "1" -- "*" GameAccount : owns  
User "1" -- "*" TransactionHistory : buys/sells  
User "1" -- "*" PaymentHistory : makes payments  
User "1" -- "*" Review : writes reviews  
User "1" -- "*" Message : sends/receives messages  
  
@enduml  
