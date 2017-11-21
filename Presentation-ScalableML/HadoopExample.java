/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ratingDeviation;

import java.io.IOException;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

/**
 *
 * @author Sc Zhang
 */
public class ratingDeviation {
    
    public static class MapperMovies extends Mapper<Object, Text, Text, DoubleWritable> {
    
        private final static DoubleWritable rating = new DoubleWritable();
        private Text movie = new Text();
        
        
        @Override
        public void map(Object key, Text value, Context context) 
        throws IOException, InterruptedException{
            String line = value.toString();
            String[] splits = line.split("::");
            if(line != null && !line.isEmpty() && line.length() >= 4) {
            
                movie.set(splits[1]);
                rating.set(Integer.valueOf(splits[2]));
                context.write(movie, rating);
            }
        }
    
    }
    
    public static class ReducerMovies extends Reducer<Text, DoubleWritable, Text, DoubleWritable> {
        
        private DoubleWritable result = new DoubleWritable();
        
        @Override
        public void reduce(Text key, Iterable<DoubleWritable> values, Context context) 
        throws IOException, InterruptedException {
            double sum = 0;
            int count = 0;
            double average = 0;
            double median = 0;
            double standard =0;
            double standardSum =0;
            
            
            for (DoubleWritable value : values) {
                sum += value.get();
                count++; 
            }
            
            double ratingList[] = new double[count];
            
            average = sum * 1.0 / count;
            
            for (DoubleWritable value : values) {
                double x =value.get();
                standardSum += Math.pow(x-average, 2);
            }
            standard = Math.sqrt(standardSum/count);
            
            if(count%2>0){
                median = ratingList[count/2 + 1];
            } else{
                median = ratingList[count/2];
            }
            
            
            result.set(standard);
            context.write(key, result);
        }
    }
            
    
    public static void main(String[] args) throws IOException, InterruptedException, ClassNotFoundException{
        // TODO code application logic here
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "rated movies");
        job.setJarByClass(ratingDeviation.class);
        job.setMapperClass(MapperMovies.class);
        job.setCombinerClass(ReducerMovies.class);
        job.setReducerClass(ReducerMovies.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
