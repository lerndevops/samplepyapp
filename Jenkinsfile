pipeline {
   agent any
   stages {
     stage('configure-env'){
       steps{
          git branch: 'main', url: 'https://github.com/lerndevops/samplepyapp'
          sh 'pyb install_dependencies'
       }
     }
     stage('compile'){
       steps{
          sh 'pyb compile_sources'
       }
    }
    stage('codereview'){
      steps{
         sh 'pyb analyze'
      }
      post{
        success {
           recordIssues(tools: [flake8(pattern: '**/target/reports/flake8')])
        }
      }
   }
   stage('unittest'){
     steps{
        sh 'pyb run_unit_tests'
     }
     post{
       success{
          junit '**/target/reports/*.xml'
       }
     }
   }
   stage('coverage'){
     steps{
        sh 'pyb coverage'
     }
     post{
       success{
          cobertura autoUpdateHealth: false, autoUpdateStability: false, coberturaReportFile: '**/target/reports/*_coverage.xml', conditionalCoverageTargets: '70, 0, 0', failUnhealthy: false, failUnstable: false, lineCoverageTargets: '80, 0, 0', maxNumberOfBuilds: 0, methodCoverageTargets: '80, 0, 0', onlyStable: false, sourceEncoding: 'ASCII', zoomCoverageChart: false
       }
     }
   }
   stage('package'){
     steps{
        sh 'pyb package'
     }
   }
   }
}
