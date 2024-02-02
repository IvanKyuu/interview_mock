# Mock Interview Question
# 步骤
## 公司介绍
华为
## Team分工
### BQ (Behaviour Question) 提问
1. **Q**: 你为啥想来我们公司/你对我们公司有什么了解：
   **A**: 1. 企业了解，文化，分工，成绩
      1. 如果可以的话，扯一点你跟公司本来的关系是好的
         1. 你之前关注过这个公司
         2. 你之前和他们合作的经验
2. **Q**: 之前解决过什么问题：
   **A**: 
____
### Academical Skills
1. What are the different data types present in C++?
* Primitive Datatype(basic datatype). Example- char, short, int, float, long, double, bool, etc.
* Derived datatype. Example- array, pointer, etc.
* Enumeration. Example- enum 枚举类
* User-defined data types. Example- structure, class, etc.

1. What is the difference between C and C++?
   1. **c: pop (procedure-opiented programming)
     c++: oop (object-oriented programming)**
      1. oop 特性：抽象（abstraction），封装（encapsulation），多态（Polymorphism）
         1. 抽象：user only need to know / tell c++ "what to do" without telling how to do it. 
            1. 数据抽象attribute
            2. 过程抽象
         2. 封装：封装，即隐藏对象的属性attribute和实现细节，仅对外公开接口，控制程序对类属性的读取和修改。
            1. 对于类的内部，成员函数可以自由修改成员变量，进行更精确的控制；
            2. 对于类的外部，良好的封装能够减少耦合，同时隐藏实现细节。
         3. 多态：子类class的指针可以给父类。
            1. Example: `Parent obj = Child(name ="child");`
            2. 怎么体现：调用父类指针，不同子类实例体现不同效果。
               1. 狗叫汪汪，猫叫喵喵
                  1. 都可以调用叫的接口
   2. C does not support data hiding. C++: Data is hidden by encapsulation to ensure that data structures and operators are used as intended.
   3. C is a subset（子集） of C++，C++是C的superset（父级）。
   4. Function and operator overloading are not supported in C. Function and operator overloading is supported in C++，符号重（超过）载。
      1. override：重写。
   5. Namespace features are not present in C。Namespace is used by C++, which avoids name collisions.
   6. Functions can not be defined inside structures of c.Functions can be defined inside structures of C++. C++中attribute可以包含函数。
   7. c: calloc() and malloc() functions are used for memory allocation and free() function is used for memory deallocation.
      1. c++: new operator is used for memory allocation and deletes operator is used for memory deallocation.
      2. new, delete 是malloc和free的wrapper。
___
1.  What are class and object in C++?
    1.  Class: A class is a user-defined data type that has data members and member functions. Data members are the data variables and member functions are the functions that are used to perform operations on these variables.
    2.  Object: An instance(实例) of a class. 实例才占用内存。
        1.  Example:
            1.  `Class Dog : public Class Animal {}` 所有的狗。
            2.  Object: `Dog mydog = Dog();` 家里养的那条。
2. What is the difference between struct and class?
   | Structre | Class |
   |----------|-------|
   |Members of the structure are public by default. | Members of the class are private by default.|
   |When deriving a struct from a class/struct, default access specifiers for base class/struct are public. | When deriving a class, default access specifiers are private.|
3. What is operator overloading?
   1. Operator Overloading is a very essential element to perform the operations on user-defined data types. By operator overloading we can modify the default meaning to the operators like +, -, *, /, <=, etc. 
       1. 改变函数签名。
          1. 要么改变函数参数列表的参数类型，要么改变参数数量。
          2. return type, exception无法改变函数签名。
