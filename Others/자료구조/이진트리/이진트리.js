class Node
{
    constructor(data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

function makingTree(arr, root, i)
{
    if (i < arr.length)
    {
        root = new Node(arr[i]);
        root.left = makingTree(arr, root.left, 2*i + 1);
        root.right = makingTree(arr, root.right, 2*i + 2);
    }
    
    return root;
}

let arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
let root;

let root_tree = makingTree(arr, root, 0)

/*                                                                           */
// function Inoder(root)
// {
//     let answer = [];

//     let left_temp = root;
//     let right_temp = root;

//     while(left_temp.left != null)
//         left_temp = left_temp.left

//     while(right_temp.right != null)
//         right_temp = right_temp.right
    
//     console.log(left_temp)
//     console.log(right_temp)
// }

/*                                                                           */
function Inorder(root, answer)
{
    
    if(root.left != null)
        Inorder(root.left, answer)

    answer.push(root.data)
    
    if(root.right != null)
        Inorder(root.right, answer)


}


let answer  = []

Inorder(root_tree, answer)
console.log(arr)
console.log(answer)
