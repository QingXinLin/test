import com.fcibook.quick.http.QuickHttp


class ls3{

}
object ls3{

  def main(args: Array[String]) {
    println("hello scala");
    System.out.println("hello world'")
    println("a\t\nb")
    val a=3  //int
    val b="nihao" //string
    val c=3.4d   //float=Float.Double精确度高
    val d=3.4f   // Float
    val e=true  //Bloolean
    val f=Array(1,3,4,3,4,4)  //Array数组，list
    val g=Array(1,"a","b")  //如果没有限制类型，放容易，拿不容易，降低性能
    val g1=Array[Int](1,3,3)  //A仍然有【限制类型】（参数列表）
    println(a+b+c+d+e+f+g+g1)
    val h = Tuple2(1,2)  //元组类型
    val f2=List(1,2,3,4,43)
    //    println(f2[0])  //获取列表中的元素
    println("获取列表中的元素："+f2(0))
    //  java与scala的占位符是%s，python占位符是{}
    val x="今天星期%s，我很%s".format("6","6")
    println("字符串的占位符的使用："+x)


  }
}


object ls2{
  def main(args: Array[String]) {
    println("hello scala");
    System.out.println("hello world'")
    println("a\t\nb")
    val a:Int=3  //int
    val b:String="nihao" //string
    val c:Double=3.4d   //float=Float.Double精确度高
    val d:Float=3.4f   // Float
    val e:Boolean=true  //Bloolean
    // 原理是：苹果不等于水果,水果【苹果】=苹果
    val f:Array[Int]=Array(1,3,4,3,4,4)  //Array数组，list
    val g:Array[Any]=Array(1,"a","b")  //如果没有限制类型，放容易，拿不容易，降低性能
    val g1:Array[Int]=Array[Int](1,3,3)  //A仍然有【限制类型】（参数列表）
    println(a+b+c+d+e+f+g+g1)
    val h:Tuple2[Int,Int]=Tuple2(1,2)  //元组类型
    val f2:List[Int]=List(1,2,3,4,43)
    //    println(f2[0])  //获取列表中的元素
    println("获取列表中的元素："+f2(0))
    //  java与scala的占位符是%s，python占位符是{}
    val x:String="今天星期%s，我很%s".format("6","6")
    println("字符串的占位符的使用："+x)


  }

}
object LHAFAA {
  def main(args: Array[String]): Unit = {
    val url = "http://www.gaokaopai.com/university-ajaxGetMajor.html"
    val info=new QuickHttp()
      .url(url)
      .get()
      .addHeader("X-Requested-With", "XMLHttpRequest")
      .addHeader("connection", "Keep-Alive")
      .addHeader("user-agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")
      .text()
    println(info)
  }
}



