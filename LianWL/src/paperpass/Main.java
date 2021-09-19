package paperpass;

import java.io.File;
import java.text.DecimalFormat;

public class Main {

    public static void main(String[] args){
        Main txtCheck = new Main();

        if(args.length !=0){
            txtCheck.Test1(args[0],args[1],args[2]);
        }else{
            txtCheck.Test1("text2\\orig.txt","text2\\orig_0.8_dis_10.txt","output.txt");

//            PathInput.pathInput();
        }

    }






    public void Test1(String origin,String textPath,String outPath){

        try {
            SimHash hash1 = new SimHash(IOText.getText(origin),  64 );
            SimHash hash2 = new SimHash(IOText.getText(textPath),  64 );

            // 计算 海明距离 在 3 以内的各块签名的 hash 值
            hash1.subByDistance(hash1, 3);
            hash2.subByDistance(hash2, 3);
            // 计算两个签名的海明距离
            int  distance = hash1.getDistance(hash1.getStrSimHash(),hash2.getStrSimHash());
            DecimalFormat decimalFormat = new DecimalFormat("0.00");
            double similarity = 0;
            if(distance != -2){
                similarity = (100-distance*100/128);
            }
            System.out.println("\r\n抄袭文本"+ textPath +"与原文:"+origin+"的相似度为"+similarity+"%");

            String content = "\r\n抄袭文本文件的路径：" + textPath + "\r\n原文的路径：" + origin + "\r\n文本相似率为" + decimalFormat.format(similarity)+"%";

            IOText.writeText(content,outPath);

        }catch(Exception e) {
            e.printStackTrace();
        }
    }


}


