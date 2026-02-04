# Programming Pricniples Used in This Project

This project follows fundamental programming and object-oriented programming principles. Each principle is demonstrated with direct references to specific files and lines of code in the repository.

---

## 1. Single Responsibility Principles (SRP)

Each class has a single, clearly defined responsibility.

For example, the [DecimalToRoman class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task7.py#L1-L22) is responsible only for working with decimal numbers, while the [RomanToDecimal class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task7.py#L25-L66) handles Roman numeral validation and conversion.

---

## 2. Encapsulation

Encapsulation is used to hide the internal state of objects and allow access only through class methods.

For instance, in the [Bank class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task1.py#L1-L33) the balance and operations are stored in private fields ([lines 2–5](https://github.com/ipz241shvo/kpz-lab1/blob/main/task1.py#L2-L5)) and can be modified only via public methods ([lines 7–25](https://github.com/ipz241shvo/kpz-lab1/blob/main/task1.py#L7-L27)).

---

## 3. Inheritance

Inheritance is used to extend base class functionality without duplicating code.

An example of this is the [Admin class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task9/admin.py#L23-L26), which inherits from the [User class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task9/user.py#L1-L26).  
Another example is the [Discount class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task8/shop.py#L36-L50), which inherits from the [Shop base class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task8/shop.py#L1-L33).

---

## 4. Polymorphism

Polymorphism allows the same method to work with different objects.

For example, the `show_info()` method is used for different instances of the [Dog class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task4.py#L5-L20), producing output depending on the specific object.

---

## 5. Composition

Composition is used when one class contains objects of another class as part of its structure.

This can be seen in the [Pets class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task4.py#L20-L59), which stores and manages a list of `Dog` objects.

---

## 6. Custom Exceptions and Error Handling

The project uses custom exceptions to handle invalid input and runtime errors.

A custom exception, [NameLengthError](https://github.com/ipz241shvo/kpz-lab1/blob/main/task6.py#L1-L10), is used to validate the length of a name and ensure correct input.

---

## 7. Defensive Programming

Defensive programming techniques are applied to validate input data before processing.

For example, Roman numeral validation is implemented in the [RomanNumber class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task7.py#L70-L94), and value checks are used in the [Shop logic](https://github.com/ipz241shvo/kpz-lab1/blob/main/task8/shop.py#L19-L33) to prevent incorrect operations.

--- 

## 8. Code Reusability

The code is structured to maximize reuse and minimize duplication.

This is demonstrated by reusing the [Shop base class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task8/shop.py#L1-L35) in the [Discount class](https://github.com/ipz241shvo/kpz-lab1/blob/main/task8/shop.py#L36-L50), as well as by using common methods across multiple objects.

    