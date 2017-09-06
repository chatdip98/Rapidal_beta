package brogrammers;

import java.io.*;
import java.util.*;
import java.lang.*;


//hospital class to store different parameters.
class Hospital{
	String name;    	//name of hospital
	int bed;        	//how many beds available  
	double price;   	//price of bed 
	double rating;		//rating of the hospital in ou
	double distance;	//distance of the hospital from current location
	String disease;		//parts which is affected
	
	// contructor of the class Hospital
	Hospital(String name, int bed, double price, double rating,
			 double distance, String disease){
		
		this.name = name;
		this.bed = bed;
		this.price = price;
		this.rating = rating;
		this.distance = distance;
		this.disease= disease;
	}
}

//comparator for sorting
class normaliseComp implements Comparator<Hospital>{
	@Override
    public int compare(Hospital a, Hospital b){
		
		//normalization function (2.5*R)/D
		if ((2.5 * a.rating) / (double)a.distance < (2.5 * b.rating) / (double)b.distance ){
            return 1;
            
        } 
		else {
            return -1;
        }
	}
	
  }

public class hackathon{
	
	//driver function 
	public static void main(String[] args) throws IOException{
	
	//for taking user input and reading from database
	Scanner a = new Scanner(System.in);
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	BufferedReader br1 = new BufferedReader(new FileReader("name.txt"));
	BufferedReader br2 = new BufferedReader(new FileReader("bed.txt"));
	BufferedReader br3 = new BufferedReader(new FileReader("price.txt"));
	BufferedReader br4 = new BufferedReader(new FileReader("rating.txt"));
	BufferedReader br5 = new BufferedReader(new FileReader("distance.txt"));
	BufferedReader br6 = new BufferedReader(new FileReader("disease.txt"));
	
	//variables for storing parametes of the class hospital
	String s[] = new String[6];
	LinkedList<Hospital> hos = new LinkedList<Hospital>();
	//loop to take data from database 
	while ((s[0] = br1.readLine()) != null && (s[1] = br2.readLine()) != null && 
		  (s[2] = br3.readLine()) != null && (s[3] = br4.readLine()) != null &&
		  (s[4] = br5.readLine()) != null && (s[5] = br6.readLine()) != null  ){
		
	   Hospital h = new Hospital(s[0], Integer.parseInt(s[1]), Double.parseDouble(s[2]),
			        Double.parseDouble(s[3]), Double.parseDouble(s[4]), s[5]);
	   
	   hos.add(h);
	}
	//mapping disease to the hospital list
	HashMap<String, LinkedList<Hospital>> dmap = new HashMap<String, LinkedList<Hospital>>();
	
	for (Hospital x : hos){
		
		if (dmap.containsKey(x.disease) && x.bed != 0){
			
			LinkedList<Hospital> temp = dmap.get(x.disease);
			
			temp.add(x);
			
			dmap.replace(x.disease, temp);
			}
		else if (x.bed != 0){
			LinkedList<Hospital> temp = new LinkedList<Hospital>();
			
			temp.add(x);
			
			dmap.put(x.disease, temp);
		}
	}
	
	//user queries
	  String inputdisease = a.nextLine();
	  int inputprice = a.nextInt();
	  
	  // get hospital LIST mapped to diseases
	  LinkedList<Hospital> get = dmap.get(inputdisease);
	  
	  //sorting function of the list
	  Collections.sort(get, new normaliseComp());
	
	  boolean b = true;
	  int count = 0;
	  int term = 0;
	  
	  //print to display the recommendation
	while (b){
	
		if (get.get(term).rating > 5 && get.get(term).price < inputprice){
			
		count ++;
		
		System.out.println(count + ")" + "Name : " + get.get(term).name);
		System.out.println("Distance : " + get.get(term).distance);
		System.out.println("Price : " + get.get(term).price);
		System.out.println("Rating : " + get.get(term).rating);
		System.out.println("");
		}
		
		term ++;
		if (count == 10 || term > get.size() - 1)
			b = !b;
	}
	}
}
