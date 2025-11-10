pragma solidity ^0.8.0;

contract StudentRecord{
    struct Student{
        uint256 studentID;
        string name;
        uint256 marks;
    }

    Student public student;

    function setStudent(uint256 _id,string memory _name,uint256 _marks)public{
        student=Student(_id,_name,_marks);
    }
    function getStudent()public view returns(uint256,string memory,uint256){
        return (student.studentID,student.name,student.marks);
    }   
}