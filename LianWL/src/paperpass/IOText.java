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
    public static StringBuffer getText(String txtPath) {
        File file = new File(txtPath);

        if(file.isFile() && file.exists()){//如果文件存在
            try (FileInputStream FileinputStream = new FileInputStream(file);
                 InputStreamReader inputStreamReader = new InputStreamReader(FileinputStream);
                 BufferedReader bufferedReader = new BufferedReader(inputStreamReader);){
                //流输入
                StringBuffer strBuf = new StringBuffer();
                String text = null;
                while((text = bufferedReader.readLine()) != null){
                    strBuf.append(text);
                }
                return strBuf;
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return null;
    }


    /**写入txt文件*/
    public static void writeText(String outPath,String content,File file){
        try (FileOutputStream fileOutputStream = new FileOutputStream(file);){
            if(!file.exists()){
                //判断文件是否存在，如果不存在就新建一个txt
                file.createNewFile();
            }
            fileOutputStream.write(content.getBytes());
            fileOutputStream.flush();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

}
