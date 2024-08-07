Welcome to your new dbt project!

### Using the project
Try running the following command:
```bash
docker run --rm -e AWS_SECRET_ACCESS_KEY='...' -e AWS_ACCESS_KEY_ID='...' -e S3_BUCKET_NAME='...' -e DBT_PROFILES_DIR='/.dbt' -e DBT_COMMAND='dbt run -s stg_customers+' -v /Users/user/.dbt:/.dbt my_dbt_project
```

### Uploading to S3 bucket
After a successful dbt run, container uploads manifest.json to specified s3 bucket (you must provide it via -e argument)

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices

### Todo:
add env_file