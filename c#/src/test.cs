using System;
using System.Text;
using System.Collections.Generic;
using NUnit.Framework;

[TestFixture]
public class HelloWorldTest
{
    [Test, Property("Weight", 1.0), Property("Visibility", "visible")]
    public void HelloTest()
    {
        Assert.AreEqual(HelloWorld.Hello(), "Hello");
    }

    [Test, Property("Weight", 2.0), Property("Visibility", "hidden"), Property("Name", "Bye")]
    public void MyTest2()
    {
        Assert.AreEqual(HelloWorld.Bye(), "Bye");
    }
}
