
echo "workflow testing"

py.test --junitxml results.xml 
cp -r ./results.xml /var/lib/jenkins/workspace/pytest_workflow/results.xml

python -m coverage run 
python -m coverage xml -o coverage.xml

cp -r ./coverage.xml /var/lib/jenkins/workspace/pytest_workflow/coverage.xml

        
       

