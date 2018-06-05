

object LSHDict{
  def main(args: Array[String]) {
    val a=Map("手机"->"123456",
              "姓名"->"Chahce",
              "上课列表"->List("python","scala","redis","spark"))//
    println(a("手机"))
    val week=List("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    println("今天是"+week(0))
    val b=Map(("手机","123344"),("姓名","chance"))
  }
}

object LSHDICT
object LSHIF{
  def main(args: Array[String]) {
    if (true) {
      println("可选")
      println("xxxxx")
    }
    if(1>2){
      println("二选一")
  }else {
      println("else语句")
    }
    val score=80
    if(score>90){
      println("优秀")
    }else if(score>70){
      println("良好")
    }else{
      println("不及格")
    }

  }




}


object LShfor{
  def main(args: Array[String]) {
    val ls=List("当山峰没有棱角的时候",
      "\n当河水不再流",
      "\n当时间停住日夜不分",
      "\n当天地万物化为虚有")
    println(ls.length)
      for(i<-ls){
        println(i)
      }
    println("for升级和if搭配")
    for(i<-ls if(i!="当河水不再流")){
      println(i)
    }
    println("for升级和yield搭配")
    val fun1=for(i<-ls) i
    println(fun1)
    val fun2=for(i<-ls) yield i
    println(fun2.toBuffer)
  }
}