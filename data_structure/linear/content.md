##### 线性结构：

​	数据结构中的元素存在一对一的相互关系

##### 列表 (数组)

* **数组的存储、 查找 、以及时间复杂度**

  数组中的元素是存储在一块连续的内存中,而且必须 给定要存储的数据类型以及存储的长度

  * **存储类型:** 在创建时候必须声明存储的是那种的数据类型,这样数组中的元素的存储大小相同,加上是连续的存储方式,就可以依次进行查找 
  * **长度限制:** 声明长度,不能进行append操作

* **python中的列表** （注: 突破数组的两个限制 存储类型 | append等操作）

  * 实现变长(可以append以及pop)  动态扩张和动态收缩 
    * <img src="https://img2018.cnblogs.com/blog/1479985/201903/1479985-20190331144234984-1374631015.png" alt="img" style="zoom:80%;" />
    * 反之当执行pop操作时,会将剩余的元素,申请一块更小的内存,存储数据,原来开辟的内存,python会进行垃圾回收
  * 如何实现存储不同类型的元素 -> lst = [3,3.15,'alex']
    * <img src="https://img2018.cnblogs.com/blog/1479985/201903/1479985-20190331151755594-638406268.png" alt="img" style="zoom:80%;" />
    * 当修改值的时候,只是新开辟一块内存存储新的值,初始的列表内存修改新的地址
    * 此时没有引用的内存会被python回收 (引用计数的回收机制)
  * **python 列表操作的时间复杂度**
    * 存储过程虽然存在赋值的操作,但是时间复杂度为O(1)  摊还分析法(均摊)
    * 另外pop不加内容的删除是O(1) ,给定内容的删除是O(n),存在位置的改变
    * Insert也是O(n)
    * 赋值,修改等操作的时间复杂度为O(1)
