#!/bin/bash

#======================================================
# Name       : Yadwinder Singh
# Date       : 26-Jan-2017
# Purpose    : Creating a Polling Website to log people
#              opinion on an motion/agenda.
# Credit     : https://startbootstrap.com - for template
# Description: This CGI script is an interactive website
#              which will display the current status of
#              the poll and also encourge user to mark 
#              his opinion. 
#              Upon receiving the vote from the user
#              backend file is updated and user is 
#              redirected to Thank you page.
#======================================================

#======================================================
# load the library functions
#======================================================
source ./lab3lib.cgi


#======================================================
# Local Variable to hold current voting count
#======================================================
yes_count=`grep -i 'Yes' vote_count.txt|cut -d ":" -f2`
no_count=`grep -i 'No' vote_count.txt|cut -d ":" -f2`
neutral_count=`grep -i 'Neutral' vote_count.txt|cut -d ":" -f2`

#=======================================================
# Local Variable to calculate percentage of voting count
#=======================================================
let "total = $yes_count + $no_count + $neutral_count"
yes_percentage=`echo "$total $yes_count" |awk '{sum1=((100/ $1) * $2 ); print sum1}'`
no_percentage=`echo "$total $no_count" |awk '{sum1=((100/ $1) * $2 ); print sum1}'`
neutral_percentage=`echo "$yes_percentage $no_percentage" |awk '{sum1=((100-$1-$2)); print sum1}'`


#======================================================
# render the voting page if:
# => Page is first time loaded 
# => Or User has not cast it vote
#======================================================
if [ "x$optionsRadios" = "x" ]; then
       
cat << EOF
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>University Polling</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <!-- Bootstrap Core CSS -->
    <link href="bootstrap.min.css" rel="stylesheet">
    <!-- Custom CSS -->
    <link href="sb-admin.css" rel="stylesheet">
</head>

<body>
    <div id="page-wrapper" style="background-color: smokewhite">
        <div class="container-fluid">
            <!-- Page Heading -->
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="page-header" style="text-align: center;">
                       Cast You Vote
                    </h1>
                </div>
            </div>

            <div class="well" style="height: 70px; text-align: center; margin-top: 20px">
                <h4>Are you in favour of increasing fees by University for next Semester ?</h4>
            </div>
            <form action="?version=${version:=1}" method="POST" enctype="application/x-www-form-urlencoded">
                <fieldset class="form-group">
                    <div class="col-lg-4" style="text-align: center;">
                        <div class="form-check">
                            <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="optionsRadios" id="optionsRadios1" value="yes">
                                    In Favour
                            </label>
                        </div>
                    </div>
                    <div class="col-lg-4" style="text-align: center;">
                        <div class="form-check">
                            <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="optionsRadios" id="optionsRadios2" value="no">
                                    Against
                            </label>
                        </div>
                    </div>
                    <div class="col-lg-4" style="text-align: center;">
                        <div class="form-check disabled">
                            <label class="form-check-label">
                                <input type="radio" class="form-check-input" name="optionsRadios" id="optionsRadios3" value="neutral" >
                                    Neutral
                             </label>
                        </div>
                    </div>
                </fieldset>
                <div class="col-lg-4">
                </div>
                <div class="col-lg-4" style="text-align: center;">
                    <button type="submit" class="btn btn-default">
                        <span class="glyphicon glyphicon-thumbs-up"></span> Mark My Vote
                     </button>
                </div>
            </form>

            <br>
            <div class="row" style="margin-top: 50px">
                <h1></h1>
                <hr>
                <h4 style="margin-left: 570px">Current Status</h4>
                <div class="row">
                <div class="col-lg-2">
                </div>
                <div class="col-lg-1">
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="panel panel-yellow">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="huge" style="text-align: center;">${yes_count}</div>
                                <div style="text-align: center;" style="text-align: center;"> Favour of Motion</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="panel panel-red">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="huge" style="text-align: center;">${no_count}</div>
                                <div style="text-align: center;">   Against Motion</div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <div class="panel panel-green">
                        <div class="panel-heading">
                            <div class="row">
                                <div class="huge" style="text-align: center;">${neutral_count}</div>
                                <div style="text-align: center;">Doesn't Care</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /.row -->
            <div class="col-lg-2">
            </div>
            <div class="col-lg-8">
                <div class="progress-bar progress-bar-warning" role="progressbar" style="width:${yes_percentage}%;">
                    ${yes_percentage}%
                </div>
                <div class="progress-bar progress-bar-danger" role="progressbar" style="width: ${no_percentage}%;">
                     ${no_percentage}%
                </div>
                <div class="progress-bar progress-bar-success" role="progressbar" style="width: ${neutral_percentage}%;">
                    ${neutral_percentage}%
                </div>
             </div>
            <!-- /.row -->
            <div class="container" style="height: 40px">
            </div>
		</div>
    </div>
    <!-- /#wrapper -->

    <!-- jQuery -->
    <script src="jquery.js"></script>
    <!-- Bootstrap Core JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" 
</body>

</html>
EOF

else

#-------------------------------------------
# This section will consider the user vote
# Update the backend file
# Render the user to new page
#-------------------------------------------

#==================================================================
# Increase the vote count of "Yes" in file if user Voted in favour
#==================================================================
if [ "$optionsRadios" = "yes" ]; then
    newCount=$(($yes_count + 1))
    sed "s/Yes.*/Yes:$newCount/" vote_count.txt >> local_tmp
    chmod 755 local_tmp
    cat local_tmp > vote_count.txt 
    \rm -f local_tmp
    
fi    

#==============================================================
# Increase the vote count of "No" in file if user Voted Againt
#==============================================================
if [ "$optionsRadios" = "no" ]; then
    newCount=$(($no_count + 1))
    sed "s/No.*/No:$newCount/" vote_count.txt >> local_tmp
    chmod 755 local_tmp
    cat local_tmp > vote_count.txt 
    \rm -f local_tmp
fi

#=====================================================================
# Increase the vote count of "Neutral" in file if user voted "Neutral"
#=====================================================================
if [ "$optionsRadios" = "neutral" ]; then
    newCount=$(($neutral_count + 1))
    sed "s/Neutral.*/Neutral:$newCount/" vote_count.txt >> local_tmp
    chmod 755 local_tmp
    cat local_tmp > vote_count.txt 
    \rm -f local_tmp
fi

cat << EOEB

<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>University Polling</title>
    <!-- Bootstrap Core CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
    <link href="bootstrap.min.css" rel="stylesheet">
</head>
<body>
	<div id="page-wrapper">
		<div class="container-fluid" style="height: 590px">
            <div class="container">
				<div class="well" style="text-align: center; margin-top: 150px">
               		<h2>Thank you for your Vote  <span class="glyphicon glyphicon-thumbs-up"></span></h2>
                	<h3>Your Vote Matters!!!!</h3>
            	</div>
            </div>
        </div>
    	<!-- /.container-fluid -->
	</div>
    <!-- /#wrapper -->

    <!-- jQuery -->
    <script src="jquery.js"></script>
    <!-- Bootstrap Core JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" 
</body>
</html>

EOEB

fi
