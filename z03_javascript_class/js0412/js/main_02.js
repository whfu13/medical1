$(function(){
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

    let htmlData = "";
    for(let i=0;i<no.length;i++){
        htmlData += "<tr id='"+no[i]+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        htmlData += "<td>"+no[i]+"</td>";
        htmlData += "<td>"+name[i]+"</td>";
        htmlData += "<td>"+kor[i]+"</td>";
        htmlData += "<td>"+eng[i]+"</td>";
        htmlData += "<td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td>";
        htmlData += "<td>"+avg[i]+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
    }

    $("#body").html(htmlData);

    $("#writeBtn").click(function(){
        $(".p_all").css("display","block");
    });
    $("#cancelBtn").click(function(){
        $(".p_all").css("display","none");

    });

    $("#confirmBtn").click(function(){
        console.log("이름 : "+$("#name").val());

        if($("#name").val().length<2){
            alert("이름을 입력하셔야 등록이 가능합니다.");
            $("#name").focus();
            return false;
        }
        let i_no = Math.max.apply(null,no)+1;
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2);

        let htmlData = "";
        htmlData += "<tr id='"+i_no+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
        htmlData += "<td>"+i_no+"</td>";
        htmlData += "<td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td>";
        htmlData += "<td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td>";
        htmlData += "<td>"+i_avg+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";

        $("#body").html(htmlData);

        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
        $(".p_all").css("display","none");
    
    });

    $("#allChk").click(function(){
        if($(this).is(":checked")==true){
            $(".stuChk").each(function(){
                $(this).prop("checked",true);
            })
        }else{ $(".stuChk").each(function(){
            $(this).prop("checked",false);
        })
    }
    
});

$(".delBtn").click(function(){
    console.log("현재 선택된 class id : "+$(this).parent().parent().attr("id"));
    if(confirm("정말 삭제하시겠습니까?")){
        $("#"+$(this).parent().parent().attr("id")).remove();
    }

});

$("#deleteBtn").click(function(){
    console.log("체크박스 개수 : "+$(".stuChk").length);
    console.log("체크박스에서 체크된 개수 : "+$(".stuChk:checked").length);
    console.log("체크박스에서 체크된 개수 : "+$("input:checkbox[name='stu']:checked").length);

    if($(".stuChk:checked").length<1){
        alert("삭제할 데이터를 체크해주셔야 가능합니다.");
        return false;
    }
    if(!confirm("정말 삭제하시겠습니까?")){
        return false;
    }

    $(".stuChk").each(function(){
        if($(this).is(":checked") == true){
            console.log("현재 선택된 class 값: "+$(this).val());
            console.log("현재 선택된 id 값: "+$(this).parent().parent().attr("id"));
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });
});

});