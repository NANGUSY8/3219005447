package paperpass;

import java.math.BigInteger;
import java.util.StringTokenizer;

public class SimHash {
    //定义一个表示查重特征的SimHash
    private String tokens;
    private BigInteger intSimHash;
    private String strSimHash;
    private int  hashBits = 64;
    public SimHash(String tokens) {
        this.tokens = tokens;
        this.intSimHash = this.simHash();
    }

    public SimHash(String tokens, int hashBits) {
        this.tokens = tokens;
        this.hashBits = hashBits;
        this.intSimHash = this.simHash();
    }
    public BigInteger simHash() {
        /*
         * 思路：
         * 1、将文本进行划分，按照格式分词
         * 2、将每一个分词hash为一组固定长度的数列.比如 64bit 的一个整数.
         * 3、建立一个长度为64的整数数组，对每一个分词hash后的数列进行判断,如果是1000...1,那么数组的第一位和
         *        末尾一位加1，中间的62位减一,逢1加1,逢0减1.直到把所有的分词hash数列全部判断完毕.
         * 4、对数组进行判断,大于0的记为1,小于等于0的记为0,得到一个 64bit 的签名。
         */
        int[] v = new int [this.hashBits]; //定义特征向量/数组
        // 1、将文本进行划分，按照格式分词
        StringTokenizer stringTokens = new StringTokenizer( this.tokens,"，。！、：“”");
        while (stringTokens.hasMoreTokens()) {
            String temp = stringTokens.nextToken();
            //2、将每一个分词hash为一组固定长度的数列.比如 64bit 的一个整数.
            BigInteger t = this.hash(temp);
            for ( int i = 0; i < this.hashBits; i++) {
                BigInteger bitmask = new BigInteger( "1" ).shiftLeft(i);
               /* 3、建立一个长度为64的整数数组，对每一个分词hash后的数列进行判断,如果是1000...1,那么数组的第一位和
             末尾一位加1，中间的62位减一,逢1加1,逢0减1.直到把所有的分词hash数列全部判断完毕.*/
                if (t.and(bitmask).signum() !=  0 ) {
                    // 计算整个文档的所有特征的向量和
                    // 这里实际使用中需要 +- 权重，而不是简单的 +1/-1，
                    v[i] += 1 ;
                } else  {
                    v[i] -= 1 ;
                }
            }
        }
        BigInteger fingerPrint = new  BigInteger( "0" );
        StringBuilder simHashBuilder = new  StringBuilder();
        for ( int i = 0 ; i < this.hashBits; i++) {
            // 4、对数组进行判断,大于0的记为1,小于等于0的记为0,得到一个 64bit 的签名。
            if (v[i] >= 0 ) {
                fingerPrint = fingerPrint.add( new BigInteger( "1" ).shiftLeft(i));
                simHashBuilder.append( "1" );
            } else  {
                simHashBuilder.append( "0" );
            }
        }
        this.strSimHash = simHashBuilder.toString();
//        System.out.println(this.strSimHash + " length " + this.strSimHash.length());
        return fingerPrint;
    }

    private BigInteger hash(String source) {
        if (source == null || source.length() == 0 ) {
            return new  BigInteger( "0" );
        } else {
            char [] sourceArray = source.toCharArray();
            BigInteger x = BigInteger.valueOf((( long ) sourceArray[ 0 ]) <<  7 );
            BigInteger m = new  BigInteger( "1000003" );
            BigInteger mask = new  BigInteger( "2" ).pow( this .hashBits).subtract( new BigInteger( "1" ));
            for ( char  item : sourceArray) {
                BigInteger temp = BigInteger.valueOf(( long ) item);
                x = x.multiply(m).xor(temp).and(mask);
            }
            x = x.xor( new BigInteger(String.valueOf(source.length())));
            if (x.equals( new  BigInteger( "-1" ))) {
                x = new  BigInteger( "-2" );
            }
            return x;
        }
    }
}
