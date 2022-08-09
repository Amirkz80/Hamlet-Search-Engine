import Link from "next/link"

const Result = ({ title, summary }) => {
    const link = summary /*`http://localhost:5000/files/${title}`*/

    return (
        <div className="flex flex-col p-4 mb-4 w-full rounded-lg hover:shadow-lg">
            <Link href={link}>
                <a
                    className="font-bold text-left text-blue-700 hover:underline"
                    target="blank"
                >
                    {title}
                </a>
            </Link>
            <p className="text-gray-600">{summary}</p>
        </div>
    )
}

export default Result
