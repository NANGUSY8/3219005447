package paperpass;

import org.junit.jupiter.api.Test;

class MyTest {
    String origin = "text2\\orig.txt";
    String[] txtPath={
            "text2\\orig_0.8_add.txt",
            "text2\\orig_0.8_del.txt",
            "text2\\orig_0.8_dis_1.txt",
            "text2\\orig_0.8_dis_10.txt",
            "text2\\orig_0.8_dis_15.txt",
    };

    String[] htmlPath={
            "text\\orig_0.8_del.txt",
            "text\\orig_0.8_dis_1.txt",
            "text\\orig_0.8_dis_10.txt",
            "text\\orig_0.8_dis_15.txt",
    };

    String outPath = "output.txt";
    Main txtCheck1 = new Main();

    @Test
    public void addTest(){
        txtCheck1.Test1(origin, txtPath[0],outPath);
    }

    //文本测试
    @Test
    public void delTest(){
        txtCheck1.Test1(origin, txtPath[1],outPath);
    }

    @Test
    public void dis_1Test(){
        txtCheck1.Test1(origin, txtPath[2],outPath);
    }

    @Test
    public void dis_10Test(){
        txtCheck1.Test1(origin, txtPath[3],outPath);
    }

    @Test
    public void dis_15Test(){
        txtCheck1.Test1(origin, txtPath[4],outPath);
    }

    //html测试
    @Test
    public void html1Test(){
        txtCheck1.Test1(htmlPath[0], htmlPath[1],outPath);
    }

    @Test
    public void html2Test(){
        txtCheck1.Test1(htmlPath[0], htmlPath[2],outPath);
    }

    @Test
    public void html3Test(){
        txtCheck1.Test1(htmlPath[0], htmlPath[3],outPath);
    }

    @Test
    public void html4Test(){
        txtCheck1.Test1(htmlPath[1], htmlPath[2],outPath);
    }

    @Test
    public void html5Test(){
        txtCheck1.Test1(htmlPath[1], htmlPath[3],outPath);
    }

    /*
    //@Test
    public void testExample(){
        myTest();
    }

    public void myTest(){

        Main txtCheck1 = new Main();

        txtCheck1.Test1(origin, txtPath[1],outPath);
        txtCheck1.Test1(origin, txtPath[2],outPath);
        txtCheck1.Test1(origin, txtPath[3],outPath);
        txtCheck1.Test1(origin, txtPath[4],outPath);

//        txtCheck1.Test1(htmlPath[0], htmlPath[1],outPath);
//        txtCheck1.Test1(htmlPath[0], htmlPath[2],outPath);
//        txtCheck1.Test1(htmlPath[0], htmlPath[3],outPath);
//        txtCheck1.Test1(htmlPath[1], htmlPath[2],outPath);
//        txtCheck1.Test1(htmlPath[1], htmlPath[3],outPath);

        PathInput obj = new PathInput();
        obj.pathInput();
    }
*/

}