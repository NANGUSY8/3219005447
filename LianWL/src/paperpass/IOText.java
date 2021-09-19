package paperpass;

import java.io.BufferedReader;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;

import java.io.InputStreamReader;

public class IOText {
    /**传入txt路径读取txt文件
     * @param
     * @return 返回读取到的内容
     */
    public static String getText(String txtPath) {File file = new File(txtPath);
        StringBuffer strBuf = new StringBuffer("");

        if (!file.exists()){
            System.out.print(txtPath + "文件不存在或路径错误\n");
            return null;
        }

            try (FileInputStream FileinputStream = new FileInputStream(file);
                 InputStreamReader inputStreamReader = new InputStreamReader(FileinputStream);
                 BufferedReader bufferedReader = new BufferedReader(inputStreamReader);){
                //流输入
                String text = null;
                int len = 0;
                while((text = bufferedReader.readLine()) != null){
                   if(len != 0){
                       strBuf.append("\r\n"+text);
                   }else{
                       strBuf.append(text);
                   }
                   len++;
                }
                if (strBuf.isEmpty()){
                    System.out.print(txtPath + "文件内容为空\n");
                }
            } catch (Exception e) {
                System.out.print(txtPath + "文件不存在或路径错误\n");
                e.printStackTrace();
            }

        return strBuf.toString();
    }


    /**写入txt文件*/
    public static void writeText(String content,String outPath){
        File file = new File(outPath);
        if (!file.exists()){
            System.out.print(outPath + "文件不存在或路径错误!输出失败!\n");
        }else{
            try (FileOutputStream fileOutputStream = new FileOutputStream(file);) {

                fileOutputStream.write(content.getBytes());
                fileOutputStream.flush();
            } catch (Exception e) {
                System.out.print("文件不存在或路径错误");
                e.printStackTrace();
            }
        }



    }

}
