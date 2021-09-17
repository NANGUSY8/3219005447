package paperpass;

import java.io.File;
import java.text.DecimalFormat;

public class Test {

    public static void main(String[]args){
        Test txtCheck = new Test();

        if(args.length !=0){
            args = new String[3];
            txtCheck.Test1(args[0], args[1],args[2]);
        }else{
            //测试用例
            txtCheck.myTest();
        }





    }

    public void myTest(){
        String origin = "D:\\APP\\JAVA\\text2\\orig.txt";
        String[] txtPath={
                "D:\\APP\\JAVA\\text2\\orig_0.8_add.txt",
                "D:\\APP\\JAVA\\text2\\orig_0.8_del.txt",
                "D:\\APP\\JAVA\\text2\\orig_0.8_dis_1.txt",
                "D:\\APP\\JAVA\\text2\\orig_0.8_dis_10.txt",
                "D:\\APP\\JAVA\\text2\\orig_0.8_dis_15.txt",
        };

        String[] htmlPath={
                "D:\\APP\\JAVA\\text\\orig_0.8_del.txt",
                "D:\\APP\\JAVA\\text\\orig_0.8_dis_1.txt",
                "D:\\APP\\JAVA\\text\\orig_0.8_dis_10.txt",
                "D:\\APP\\JAVA\\text\\orig_0.8_dis_15.txt",
        };

        String outPath = "D:\\APP\\JAVA\\output.txt";

        Test txtCheck1 = new Test();

        txtCheck1.Test1(origin, txtPath[0],outPath);
        txtCheck1.Test1(origin, txtPath[1],outPath);
        txtCheck1.Test1(origin, txtPath[2],outPath);
        txtCheck1.Test1(origin, txtPath[3],outPath);
        txtCheck1.Test1(origin, txtPath[4],outPath);

        txtCheck1.Test1(htmlPath[0], htmlPath[1],outPath);
        txtCheck1.Test1(htmlPath[0], htmlPath[2],outPath);
        txtCheck1.Test1(htmlPath[0], htmlPath[3],outPath);
        txtCheck1.Test1(htmlPath[1], htmlPath[2],outPath);
        txtCheck1.Test1(htmlPath[1], htmlPath[3],outPath);

        PathInput obj = new PathInput();
        obj.pathInput();
    }




    public void Test1(String origin,String textPath,String outPath){

        try {
            //获取文本
            StringBuffer strBuf1 = IOText.getText(origin);
            StringBuffer strBuf2 = IOText.getText(textPath);
            SimHash hash1 = new SimHash(strBuf1.toString(),  64 );
            SimHash hash2 = new SimHash(strBuf2.toString(),  64 );

            // 计算 海明距离 在 3 以内的各块签名的 hash 值
            hash1.subByDistance(hash1, 3);
            hash2.subByDistance(hash2, 3);
            // 计算两个签名的海明距离
            double distance = hash1.getDistance(hash1.getStrSimHash(),hash2.getStrSimHash());
            DecimalFormat decimalFormat = new DecimalFormat("0.00");
            System.out.println("抄袭文本"+ textPath +" 与原文:"+origin+"的相似度为"+((distance/64.0)*100)+"%");

            //写入答案文件中
            File file = new File(outPath);
            String content = "\r\n抄袭文本文件的路径：" + textPath + "\r\n原文的路径：" + origin + "\r\n文本相似率为" + decimalFormat.format(((distance/64.0)*100))+"%";

            IOText.writeText(outPath, content,file);

        }catch (NullPointerException e1) {
            System.out.println("输入路径错误或文件不存在");
            e1.printStackTrace();
        } catch (Exception e) {
            System.out.println("输入错误导致程序出错");
            e.printStackTrace();
        }
    }


}


