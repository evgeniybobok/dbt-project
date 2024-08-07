Welcome to dbt project!

### Using the project
Try running the following command:
```bash
docker run --rm -v /Users/$USER/.dbt:/.dbt --env-file .env -e DBT_COMMAND='dbt run -s stg_customers+' my_dbt_project
```

### Uploading to S3 bucket
After a successful dbt run, container uploads manifest.json to specified s3 bucket (you must provide it in ```.env``` file)

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
