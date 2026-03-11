# OOPJ Notes Day-5 (02 March, 2026)

## Interfaces and their Implementations

- Interface is a **blueprint of a class** that contains only abstract methods and constants.
- It is used to achieve **abstraction and multiple inheritance** in Java.
- An interface can be implemented by any class, from any inheritance tree.
- Example:

```java
interface Drawable {
    void draw();
}
class Circle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing a circle");
    }
}
class Rectangle implements Drawable {
    @Override
    public void draw() {
        System.out.println("Drawing a rectangle");
    }
}

public class Program {
    public static void main(String[] args) {
        Drawable d1 = new Circle();
        Drawable d2 = new Rectangle();

        d1.draw(); // Output: Drawing a circle
        d2.draw(); // Output: Drawing a rectangle
    }
}
```

---

### Types of Interfaces

1. Functional Interface
2. Marker Interface
3. Normal Interface

#### Functional Interface

- Contains exactly one abstract method.
- Used for lambda expressions and method references.
Example:

```java
@FunctionalInterface
interface MyFunctionalInterface {
    void myMethod();
}
```

#### Marker Interface

- Contains no methods or constants.
- Used to indicate that a class has a certain property or behavior.

Example:

```java
interface Serializable {
}
```

#### Normal Interface

- Contains multiple abstract methods and constants.
Example:

```java
interface MyInterface {
    void method1();
    void method2();
    int CONSTANT = 100;
}

class MyClass implements MyInterface {
    @Override
    public void method1() {
        System.out.println("Method 1 implementation");
    }

    @Override
    public void method2() {
        System.out.println("Method 2 implementation");
    }
}

class Program {
    public static void main(String[] args) {
        MyInterface obj = new MyClass();
        obj.method1(); // Output: Method 1 implementation
        obj.method2(); // Output: Method 2 implementation
        System.out.println(MyInterface.CONSTANT); // Output: 100
    }
}   

```

#### Things to remember about interfaces

- Cannot be instantiated
- Can contain only abstract methods and constants (before Java 8)
- Can be implemented by any class
- Supports multiple inheritance
- Can have default and static methods (since Java 8)
- Can have private methods (since Java 9)

## Exception Handling in Java

### Exception Concept

- Definition
  - Exception is an issue / unexpected event / instance which occurs during execution of application.
  - Exception is an instance which is used to acknowledge user of the system if any exeption situation occurs in the code.
  - If we want to manages OS resources carefully then we should use exception handling in Java.
- Throwable class Hierarchy
  - java.lang.Object is ultimate super class of all the classes in Java language.
  - Methods of java.lang.Object class:
    - public String toString( );
    - public boolean equals( Object obj );
    - public native int hashCode();
    - protected native Object clone( )throws CloneNotSupportedException
    - protected void finalize( )throws Throwable;
    - public final native Class<?> getClass();
    - public final void wait( )throws InterruptedException
    - public final native void wait( long timeOut )throws InterruptedException
    - public final void wait( long timeOut, int nanos)throws InterruptedException
    - public final native notify( );
    - public final native notifyAll( );

- java.lang.Throwable