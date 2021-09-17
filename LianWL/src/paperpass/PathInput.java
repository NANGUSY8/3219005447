package paperpass;

import java.io.File;
import java.text.DecimalFormat;
import java.util.Scanner;

public class PathInput {

    public static void pathInput() {
        Scanner scn =null;
        try {
            scn = new Scanner(System.in);
            System.out.print("是否需要继续查询(是：1，否：0)");
            int choice = scn.nextInt();

            while (choice==1){
                System.out.print("请输入论文原文的路径:");
                String txtPath = scn.next();
                StringBuffer strBuf2 = IOText.getText(txtPath);

                System.out.print("请输入抄袭论文的路径:");
                String textPath = scn.next();
                StringBuffer strBuf1 = IOText.getText(textPath);

                SimHash hash1 = new SimHash(strBuf1.toString(),  64 );
                SimHash hash2 = new SimHash(strBuf2.toString(),  64 );

                //计算两个文档对应签名的海明距离
                int distance = hash1.getDistance(hash1.getStrSimHash() , hash2.getStrSimHash());
                DecimalFormat decimalFormat = new DecimalFormat("0.00");
                System.out.println(txtPath+"文本与"+textPath+"文本的相似度为"+decimalFormat.format(((distance/64.0)*100))+"%");

                //避免测试用例的文件内容覆盖，新建另一个答案文件
                String outPath1 = "D:\\APP\\JAVA\\output1.txt";
                File file = new File(outPath1);

                String content = "\r\n抄袭论文文件的路径：" + textPath + "\r\n论文原文的路径：" + txtPath + "\r\n论文重复率为" + decimalFormat.format(((distance/64.0)*100)+"%");
                IOText.writeText(outPath1, content,file);

                System.out.print("是否需要继续查询(是：1，否：0)");
                choice = scn.nextInt();
            }


        } catch (NullPointerException e1) {
            System.out.println("输入路径错误或文件不存在");
            e1.printStackTrace();
        } catch (Exception e) {
            System.out.println("输入错误导致程序出错");
            e.printStackTrace();
        } finally {
            if(scn != null) {
                scn.close();
            }
        }
    }

}
