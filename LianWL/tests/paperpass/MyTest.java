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
            "text\\orig_0.8_dis_1.txt", "text\\orig_0.8_dis_10.txt",
            "text\\orig_0.8_dis_15.txt",};

    String outPath = "output.txt";
    Main txtCheck1 = new Main();

    /**
    *文本测试：
     *原文件的添加
    */
    @Test
    public void addTest(){
        txtCheck1.Test1(origin, txtPath[0],outPath);
    }

    /**原文件的删除*/
    @Test
    public void delTest(){
        txtCheck1.Test1(origin, txtPath[1],outPath);
    }

    /**原文件的修改*/
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

    /**
     * 对 html 进行测试
     * */
    @Test
    public void html1Test(){
        txtCheck1.Test1(origin, htmlPath[1],outPath);
    }

    @Test
    public void html2Test(){
        txtCheck1.Test1(origin, htmlPath[3],outPath);
    }

    /**html 和 html 进行测试*/
    @Test
    public void html3Test(){
        txtCheck1.Test1(htmlPath[0], htmlPath[3],outPath);
    }

    /**
     * 测试文本路径错误或不存在
     * */
    @Test
    public void txtPathWrongTest(){
        txtCheck1.Test1("text\\orig_del.txt","text2\\orig_dis_15.txt" ,outPath);
    }

    /**
     * 输出文件路径错误或不存在
     * */
    @Test
    public void outPathWrongTest(){
        txtCheck1.Test1("text2\\orig_0.8_del.txt","text2\\orig_0.8_dis_10.txt","out_put.txt");
    }

    /**
     * 测试文本为空
     * */
    @Test
    public void emptyTest(){
        txtCheck1.Test1("text2\\empty.txt","text2\\orig_0.8_dis_10.txt","output.txt");
    }}