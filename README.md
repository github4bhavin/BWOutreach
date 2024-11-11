# BWOutreach

# how to run
1. initiate virtualenv

`virtualenv .venv`

`source .venv/bin/activate`

2. install required libraries

`pip install -r requirements`

3. run

`python main.py process /Users/bhavinpatel/Documents/BrightWheel/outreach/source_data/S1/S1.csv`


# Design

1. Each vendor drops the file in S3 within their respective directories , here it is simulated by `source_data` dir.
2. as soon as the file is uploaded to S3 , this should trigger a lambda function. AWS passess the s3 file path to this lambda function.
    
    I simulated in this code py passing the file name to the commandline switch.

3. based on the directory name , Code will decide which source module to call for processing.

    * Source module should be designed to do following:

        * provide mapping or schema of the input file along with their datatypes.
        * It should have code to generate target schema ( here the `ourteach` schema specified in the `Targets/outreach_target.py`)
        * should be implemented from the abstract class `SourceBase`.
        * should also have the source to target mapping method implemented `generate_target`. 

4. the code works as follows:

    * `SourceProcessor` reads each line from the input file. then
    * it calls the corresponding source eg: `S1` . 
    * if the input row passes validation of pydantic then it Source pydantic model is transformed into target pydantic model
    * finall the target is exported as dict which is collected and written to the output target file.

5. outfile is then batch loaded in the final database , here I have used sqlite to demonstrate that

6. and then we apply ETL , Merge data from staging to final table. Here I have just showed that we merge new data that comes in with the existing data.

    in reality we would add CDC slowly changing dims to capture changes coming from various sources instead of overwriting.

Advantages:

* by using this design we can add new inputs and their correspoding mapping to Target.
* we can add new target mappings as well, ( current code needs rework to create good source to target mapping including Versioning to handle changing schema.)


Enhancements:

* we can package the code in Docker and use image in the lambda function. Ofsoucre if the amount of data that comes in large enough that it cant be process in lambda function or that the processing would take more than 5 min. then we have to design the lambda to kick of ECS task.

* This is an event driven design but you would want to keep orchestration tool like Airflow and have  DAG in this repository for adhoc execution , backfills etc.

* Quality Control: we are preprocessing all records that gets delivered and so we can catch any errors early on in the pipeline. I ran out of time but Ideally I would like to create 2 sets after the preprocessing step. one for good records and one for bad records instead of discarding the entire file. and then let the good records flow downstream.

    * I have also shows how we can unit test each module and the final transformed model. This is very helpful for testing our mapping functions with various imputs.

* data enrichment: Enrichment can be done in two places, one int the pydentic model and other in the ETL phase where we can combine loaded data with public datasets to fill in any missing information.

* data governance:
    * we can have strict access using aws policies on data that resides in S3.
    * we can implement access congrols on mysql data.
    * ideally we should be masking email, phone, etc PII information in s3 and mysql and only make it avialable to the application by detokenizeing for the appropriate users.
    